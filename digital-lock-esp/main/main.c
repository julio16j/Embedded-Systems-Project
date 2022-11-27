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

static void wifi_event_handler(void *event_handler_arg, esp_event_base_t event_base, int32_t event_id, void *event_data)
{
    switch (event_id)
    {
        case WIFI_EVENT_STA_START:
            printf("wifi connecting... \n");
            break;
        case WIFI_EVENT_STA_CONNECTED:
            printf("wifi connected...\n");
            break;
        case WIFI_EVENT_STA_DISCONNECTED:
            printf("wifi lost connection... \n");
            break;
        case IP_EVENT_STA_GOT_IP:
            printf("Wifi got IP...\n\n");
            break;
        default:
            break;
    }
}

void get_rest_function() {
    
    esp_http_client_config_t client_configuration = {
        .url =  "http://joaohenrique.pythonanywhere.com/api/exists/123/1"
    };
    esp_http_client_handle_t client = esp_http_client_init(&client_configuration);
    esp_http_client_perform(client);
    printf("status: %d", esp_http_client_get_status_code(client));
    esp_http_client_cleanup(client);
}

void app_main(void)
{
    nvs_flash_init();

    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();
    wifi_init_config_t wifi_initiation = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&wifi_initiation);

    esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, wifi_event_handler, NULL);
    esp_event_handler_register(IP_EVENT, IP_EVENT_STA_GOT_IP, wifi_event_handler, NULL);

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
