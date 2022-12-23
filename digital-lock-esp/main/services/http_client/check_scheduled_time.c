#include <stdio.h>
#include <string.h>
#include "esp_http_client.h"

#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

#define LED_PIN_12 12
#define LED_PIN_14 14
#define LED_PIN_27 27

char *path = "api/exists/";
esp_http_client_handle_t client;
int status_code;

void fill_url_check_scheduled_time (char *filled_url, char *url, char *user_id, char *lock_id);

esp_err_t client_event_handler(esp_http_client_event_handle_t evt) {
    switch (evt->event_id)
    {
        case HTTP_EVENT_ON_DATA:
            status_code = esp_http_client_get_status_code(client);

            gpio_pad_select_gpio(LED_PIN_12);
            gpio_set_direction(LED_PIN_12, GPIO_MODE_OUTPUT);

            gpio_pad_select_gpio(LED_PIN_14);
            gpio_set_direction(LED_PIN_14, GPIO_MODE_OUTPUT);

            gpio_pad_select_gpio(LED_PIN_27);
            gpio_set_direction(LED_PIN_27, GPIO_MODE_OUTPUT);

            if (status_code == 200) {
                
                gpio_set_level(LED_PIN_12, 1);
                vTaskDelay(50 / portTICK_PERIOD_MS);

                gpio_set_level(LED_PIN_27, 1);
                vTaskDelay(50 / portTICK_PERIOD_MS);

                gpio_set_level(LED_PIN_14, 0);
                vTaskDelay(50 / portTICK_PERIOD_MS);
            }
            else {
                gpio_set_level(LED_PIN_12, 0);
                vTaskDelay(50 / portTICK_PERIOD_MS);

                gpio_set_level(LED_PIN_27, 0);
                vTaskDelay(50 / portTICK_PERIOD_MS);

                gpio_set_level(LED_PIN_14, 1);
                vTaskDelay(50 / portTICK_PERIOD_MS);
            }

            printf("status: %d\n", status_code);
            break;
        default:
            break;
    }
    return ESP_OK;
}

void check_scheduled_time(char *url, char *user_id, char *lock_id) {
    char filled_url[1000]="";
    fill_url_check_scheduled_time (filled_url, url, user_id, lock_id);
    esp_http_client_config_t client_configuration = {
        .url =  &filled_url,
        .event_handler = client_event_handler
    };
    client = esp_http_client_init(&client_configuration);
    esp_http_client_perform(client);
    esp_http_client_close(client);
    esp_http_client_cleanup(client);
}

void fill_url_check_scheduled_time (char *filled_url, char *url, char *user_id, char *lock_id) {
    strcat(filled_url, url);
    strcat(filled_url, path);
    strcat(filled_url, user_id);
    strcat(filled_url, lock_id);
}