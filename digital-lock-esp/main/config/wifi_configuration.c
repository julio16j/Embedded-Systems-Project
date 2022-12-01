#include <stdio.h>
#include <string.h>
#include "esp_wifi.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_netif.h"

#define ssid_size 32
#define password_size 64
char wifi_ssid[ssid_size] = "wifi1";
char wifi_password[password_size] = "12345678";

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

void wifi_init (char *ssid, char *password) {
    nvs_flash_init();
    esp_netif_init();
    esp_event_loop_create_default();
    esp_netif_create_default_wifi_sta();
    wifi_init_config_t wifi_initiation = WIFI_INIT_CONFIG_DEFAULT();
    esp_wifi_init(&wifi_initiation);
    esp_event_handler_register(WIFI_EVENT, ESP_EVENT_ANY_ID, wifi_event_handler, NULL);
    esp_event_handler_register(IP_EVENT, IP_EVENT_STA_GOT_IP, wifi_event_handler, NULL);
    wifi_config_t wifi_configuration = {
        .sta = {}
    };
    strncpy((char *)wifi_configuration.sta.ssid, (char *)&ssid[0], ssid_size);
    strncpy((char *)wifi_configuration.sta.password, (char *)&password[0], password_size);
    esp_wifi_set_config(ESP_IF_WIFI_STA, &wifi_configuration);
    esp_wifi_start();
    esp_wifi_connect();
}