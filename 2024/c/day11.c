#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <stdbool.h>

/* Funktion zum Einlesen der Daten */
static int32_t *get_data(const char *filename, size_t *data_size)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        (void)fprintf(stderr, "Error: Could not open file %s\n", filename);
        exit(EXIT_FAILURE);
    }

    size_t capacity = 16u;
    int32_t *data = (int32_t *)malloc(capacity * sizeof(int32_t));
    if (data == NULL)
    {
        (void)fprintf(stderr, "Error: Memory allocation failed\n");
        fclose(file);
        exit(EXIT_FAILURE);
    }

    *data_size = 0u;
    while (true)
    {
        int scan_result = fscanf(file, "%d", &data[*data_size]);
        if (scan_result != 1)
        {
            break;
        }
        (*data_size)++;
        if (*data_size >= capacity)
        {
            capacity *= 2u;
            int32_t *new_data = (int32_t *)realloc(data, capacity * sizeof(int32_t));
            if (new_data == NULL)
            {
                (void)fprintf(stderr, "Error: Memory reallocation failed\n");
                free(data);
                fclose(file);
                exit(EXIT_FAILURE);
            }
            data = new_data;
        }
    }

    (void)fclose(file);
    return data;
}

/* Hilfsfunktion zum Aufteilen einer Zahl anhand ihrer Ziffernanzahl
   statt mit sprintf und strncpy könnte man auch eine rein numerische Variante wählen,
   aber wir belassen es beim String-Ansatz, da es einfach verständlich ist.

   Diese Funktion erstellt zwei neue Integers aus einer Ganzzahl mit gerader Stellenzahl.
   Beispiel: Wert = 1234 -> left = 12, right = 34
*/
static void split_value_even_digits(int32_t value, int32_t *left_val, int32_t *right_val)
{
    char sval[32];
    (void)sprintf(sval, "%d", value);
    size_t lval = strlen(sval);

    /* Da lval laut Logik hier gerade ist, teilen wir es einfach durch 2 */
    size_t half = lval / 2u;

    char left[32];
    char right[32];

    /* strncpy ist hier sicher, da lval max 31 sein kann (Begrenzung durch sval[32]) */
    (void)strncpy(left, sval, half);
    left[half] = '\0';
    (void)strncpy(right, &sval[half], half);
    right[half] = '\0';

    *left_val = (int32_t)atoi(left);
    *right_val = (int32_t)atoi(right);
}

/* Die Hauptlogik des Problems:
   - data: Eingabedaten
   - data_size: Anzahl der Eingabedaten
   - iterations: Anzahl der Durchläufe
   Gibt die Größe des finalen Arrays zurück.
*/
static size_t solve(const int32_t *data, size_t data_size, int iterations)
{
    /* Wir starten mit einem Array, in dem die Daten liegen */
    size_t current_size = data_size;
    int32_t *current_array = (int32_t *)malloc(current_size * sizeof(int32_t));
    if (current_array == NULL)
    {
        (void)fprintf(stderr, "Error: Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }

    for (size_t i = 0; i < data_size; i++)
    {
        current_array[i] = data[i];
    }

    for (int iter = 0; iter < iterations; iter++)
    {
        (void)printf("Iteration %d, array size: %zu\n", iter + 1, current_size);
        (void)fflush(stdout);

        /* Wir wissen nicht genau, wie groß der nächste Array wird.
           Also nutzen wir eine Heuristik: im schlimmsten Fall wird jeder Wert
           in zwei Werte aufgeteilt. Dann braucht man maximal 2 * current_size Speicher.
        */
        size_t new_capacity = current_size * 2u;
        if (new_capacity == 0u)
        {
            new_capacity = 1u;
        }

        int32_t *new_array = (int32_t *)malloc(new_capacity * sizeof(int32_t));
        if (new_array == NULL)
        {
            (void)fprintf(stderr, "Error: Memory allocation failed\n");
            free(current_array);
            exit(EXIT_FAILURE);
        }

        size_t new_size = 0u;

        /* Verarbeiten des aktuellen Arrays */
        for (size_t idx = 0; idx < current_size; idx++)
        {
            int32_t value = current_array[idx];
            if (value == 0)
            {
                /* Falls Wert 0 ist, wird ein neuer Wert 1 angehängt */
                new_array[new_size] = 1;
                new_size++;
            }
            else
            {
                /* Wert in einen String umwandeln, um die Stellenzahl zu prüfen */
                char sval[32];
                (void)sprintf(sval, "%d", value);
                size_t lval = strlen(sval);

                if ((lval % 2u) == 0u)
                {
                    /* Gerade Anzahl an Ziffern -> aufteilen */
                    int32_t left_val;
                    int32_t right_val;
                    split_value_even_digits(value, &left_val, &right_val);

                    /* Füge beide Werte hinzu */
                    if (new_size + 2u > new_capacity)
                    {
                        new_capacity *= 2u;
                        int32_t *resized = (int32_t *)realloc(new_array, new_capacity * sizeof(int32_t));
                        if (resized == NULL)
                        {
                            (void)fprintf(stderr, "Error: Memory reallocation failed\n");
                            free(new_array);
                            free(current_array);
                            exit(EXIT_FAILURE);
                        }
                        new_array = resized;
                    }

                    new_array[new_size] = left_val;
                    new_size++;
                    new_array[new_size] = right_val;
                    new_size++;
                }
                else
                {
                    /* Ungerade Anzahl an Ziffern -> Wert * 2024 */
                    if (new_size + 1u > new_capacity)
                    {
                        new_capacity *= 2u;
                        int32_t *resized = (int32_t *)realloc(new_array, new_capacity * sizeof(int32_t));
                        if (resized == NULL)
                        {
                            (void)fprintf(stderr, "Error: Memory reallocation failed\n");
                            free(new_array);
                            free(current_array);
                            exit(EXIT_FAILURE);
                        }
                        new_array = resized;
                    }

                    new_array[new_size] = value * 2024;
                    new_size++;
                }
            }
        }

        /* Altes Array freigeben und auf das neue wechseln */
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

    int solution1 = (int)solve(data, data_size, 25);
    int solution2 = (int)solve(data, data_size, 75);

    free(data);

    double elapsed = (double)(clock() - start) / (double)CLOCKS_PER_SEC;
    (void)printf("Solved in %.5f Sec.\n", elapsed);
    (void)printf("solution1=%d | solution2=%d\n", solution1, solution2);

    return 0;
}
