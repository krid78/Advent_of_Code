#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <pthread.h>

/* Struktur für Thread-Argumente */
typedef struct {
    const int32_t *input;
    size_t start;
    size_t end;
    int32_t **output_data;
    size_t *output_size;
} thread_arg_t;

/* Funktion zum Einlesen der Daten aus einer Datei */
static int32_t *get_data(const char *filename, size_t *data_size)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error: Could not open file %s\n", filename);
        exit(EXIT_FAILURE);
    }

    size_t capacity = 16u;
    int32_t *data = malloc(capacity * sizeof(int32_t));
    if (data == NULL) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        fclose(file);
        exit(EXIT_FAILURE);
    }

    *data_size = 0u;
    while (1) {
        int scan_result = fscanf(file, "%d", &data[*data_size]);
        if (scan_result != 1) {
            break;
        }
        (*data_size)++;
        if (*data_size >= capacity) {
            capacity *= 2u;
            int32_t *new_data = realloc(data, capacity * sizeof(int32_t));
            if (new_data == NULL) {
                fprintf(stderr, "Error: Memory reallocation failed\n");
                free(data);
                fclose(file);
                exit(EXIT_FAILURE);
            }
            data = new_data;
        }
    }

    fclose(file);
    return data;
}

/* Hilfsfunktion zum Aufteilen einer Zahl mit gerader Stellenanzahl */
static void split_value_even_digits(int32_t value, int32_t *left_val, int32_t *right_val)
{
    char sval[32];
    sprintf(sval, "%d", value);
    size_t lval = strlen(sval);

    size_t half = lval / 2u;

    char left[32];
    char right[32];

    strncpy(left, sval, half);
    left[half] = '\0';
    strncpy(right, sval + half, half);
    right[half] = '\0';

    *left_val = (int32_t)atoi(left);
    *right_val = (int32_t)atoi(right);
}

/* Thread-Funktion zur Verarbeitung eines Chunks */
static void *process_chunk(void *arg)
{
    thread_arg_t *targ = (thread_arg_t *)arg;
    const int32_t *input = targ->input;
    size_t start = targ->start;
    size_t end = targ->end;

    /* Reserviere Speicher für Output, grob geschätzt doppelte Menge */
    size_t capacity = (end - start) * 2u + 16u;
    int32_t *out = malloc(capacity * sizeof(int32_t));
    if (out == NULL) {
        fprintf(stderr, "Error: Memory allocation failed in thread\n");
        pthread_exit(NULL);
    }
    size_t out_size = 0u;

    for (size_t i = start; i < end; i++) {
        int32_t value = input[i];
        if (value == 0) {
            /* Einfachen Wert anhängen */
            if (out_size + 1u >= capacity) {
                capacity *= 2u;
                int32_t *tmp = realloc(out, capacity * sizeof(int32_t));
                if (tmp == NULL) {
                    free(out);
                    fprintf(stderr, "Error: Realloc failed in thread\n");
                    pthread_exit(NULL);
                }
                out = tmp;
            }
            out[out_size++] = 1;
        } else {
            char sval[32];
            sprintf(sval, "%d", value);
            size_t lval = strlen(sval);

            if ((lval % 2u) == 0u) {
                /* Gerade Anzahl Ziffern -> teilen */
                int32_t left_val, right_val;
                split_value_even_digits(value, &left_val, &right_val);

                if (out_size + 2u >= capacity) {
                    capacity *= 2u;
                    int32_t *tmp = realloc(out, capacity * sizeof(int32_t));
                    if (tmp == NULL) {
                        free(out);
                        fprintf(stderr, "Error: Realloc failed in thread\n");
                        pthread_exit(NULL);
                    }
                    out = tmp;
                }

                out[out_size++] = left_val;
                out[out_size++] = right_val;
            } else {
                /* Ungerade Stellen -> multiplizieren */
                if (out_size + 1u >= capacity) {
                    capacity *= 2u;
                    int32_t *tmp = realloc(out, capacity * sizeof(int32_t));
                    if (tmp == NULL) {
                        free(out);
                        fprintf(stderr, "Error: Realloc failed in thread\n");
                        pthread_exit(NULL);
                    }
                    out = tmp;
                }

                out[out_size++] = value * 2024;
            }
        }
    }

    /* Übergabe der Ergebnisse zurück an den Hauptthread */
    *targ->output_data = out;
    *targ->output_size = out_size;

    pthread_exit(NULL);
}

/* Diese Funktion führt mehrere Iterationen aus, verarbeitet dabei das Array in Chunks
   und nutzt Threads zur Parallelisierung. */
static size_t solve(const int32_t *data, size_t data_size, int iterations, int num_threads)
{
    /* Starte mit einer Kopie der ursprünglichen Daten */
    size_t current_size = data_size;
    int32_t *current_array = malloc(current_size * sizeof(int32_t));
    if (current_array == NULL) {
        fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    for (size_t i = 0; i < data_size; i++) {
        current_array[i] = data[i];
    }

    for (int iter = 0; iter < iterations; iter++) {
        printf("Iteration %d, array size: %zu\n", iter + 1, current_size);
        fflush(stdout);

        /* Aufteilen in Chunks */
        size_t chunk_size = (current_size + (size_t)num_threads - 1u) / (size_t)num_threads;
        if (chunk_size == 0u) {
            chunk_size = 1u;
        }

        pthread_t *threads = malloc(num_threads * sizeof(pthread_t));
        thread_arg_t *args = malloc(num_threads * sizeof(thread_arg_t));

        if (threads == NULL || args == NULL) {
            fprintf(stderr, "Error: Memory allocation for threads failed\n");
            free(threads);
            free(args);
            free(current_array);
            exit(EXIT_FAILURE);
        }

        int32_t **partial_results = malloc(num_threads * sizeof(int32_t *));
        size_t *partial_sizes = malloc(num_threads * sizeof(size_t));
        if (partial_results == NULL || partial_sizes == NULL) {
            fprintf(stderr, "Error: Memory allocation for partial results failed\n");
            free(threads);
            free(args);
            free(current_array);
            free(partial_results);
            free(partial_sizes);
            exit(EXIT_FAILURE);
        }

        for (int t = 0; t < num_threads; t++) {
            size_t start = t * chunk_size;
            if (start >= current_size) {
                args[t].start = args[t].end = current_size; /* Leerer Chunk */
            } else {
                size_t end = start + chunk_size;
                if (end > current_size) {
                    end = current_size;
                }
                args[t].start = start;
                args[t].end = end;
            }
            args[t].input = current_array;
            args[t].output_data = &partial_results[t];
            args[t].output_size = &partial_sizes[t];

            pthread_create(&threads[t], NULL, process_chunk, &args[t]);
        }

        /* Auf die Ergebnisse der Threads warten */
        size_t new_size = 0u;
        for (int t = 0; t < num_threads; t++) {
            pthread_join(threads[t], NULL);
            new_size += partial_sizes[t];
        }

        /* Neues Array aus den Teilresultaten zusammensetzen */
        int32_t *new_array = malloc(new_size * sizeof(int32_t));
        if (new_array == NULL) {
            fprintf(stderr, "Error: Memory allocation for new_array failed\n");
            for (int t = 0; t < num_threads; t++) {
                free(partial_results[t]);
            }
            free(partial_results);
            free(partial_sizes);
            free(threads);
            free(args);
            free(current_array);
            exit(EXIT_FAILURE);
        }

        size_t offset = 0u;
        for (int t = 0; t < num_threads; t++) {
            memcpy(new_array + offset, partial_results[t], partial_sizes[t] * sizeof(int32_t));
            offset += partial_sizes[t];
            free(partial_results[t]);
        }

        free(partial_results);
        free(partial_sizes);
        free(threads);
        free(args);

        free(current_array);
        current_array = new_array;
        current_size = new_size;
    }

    size_t result = current_size;
    free(current_array);
    return result;
}

int main(void)
{
    clock_t start = clock();
    size_t data_size;
    int32_t *data = get_data("2024/data/day11.data", &data_size);
    // int32_t *data = get_data("2024/data/day11.test", &data_size);

    /* Beispielsweise 4 Threads nutzen */
    int solution1 = (int)solve(data, data_size, 25, 4);
    int solution2 = (int)solve(data, data_size, 75, 4);

    free(data);

    double elapsed = (double)(clock() - start) / (double)CLOCKS_PER_SEC;
    printf("Solved in %.5f Sec.\n", elapsed);
    printf("solution1=%d | solution2=%d\n", solution1, solution2);

    return 0;
}
