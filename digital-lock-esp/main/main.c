#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/timers.h"
#include "freertos/event_groups.h"
#include "esp_wifi.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_netif.h"
#include "esp_http_client.h"
#include "config/wifiConfiguration.c"

char resposta_string_servidor[50];
int status_servidor;
esp_http_client_handle_t client;

esp_err_t client_event_handler(esp_http_client_event_handle_t evt) {
    switch (evt->event_id)
    {
        case HTTP_EVENT_ON_DATA:
            strcpy (resposta_string_servidor, (char*)evt->data);
            printf("HTTP_EVENT_ON_DATA: %.*s\n", evt->data_len, (char *)evt->data);
            status_servidor = esp_http_client_get_status_code(client);
            printf("\nstatus: %d\n", status_servidor);
            break;
        default:
            break;
    }
    return ESP_OK;
}

void get_rest_function() {
    
    esp_http_client_config_t client_configuration = {
        .url =  "http://joaohenrique.pythonanywhere.com/api/exists/123/1",
        .event_handler = client_event_handler
    };
    client = esp_http_client_init(&client_configuration);
    esp_http_client_perform(client);
    esp_http_client_cleanup(client);
}

void app_main(void)
{
    wifi_init();
    wifi_config_t wifi_configuration = {
        .sta = {
            .ssid = "wifi1",
            .password = "12345678"
        }
    };
    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_configuration);
    esp_wifi_start();
    esp_wifi_connect();
    vTaskDelay(5000 / portTICK_PERIOD_MS);
    get_rest_function();
}
