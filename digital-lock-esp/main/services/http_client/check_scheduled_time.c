#include <stdio.h>
#include <string.h>
#include "esp_http_client.h"

char *path = "api/exists/";
esp_http_client_handle_t client;
int status_code;

void fill_url_check_scheduled_time (char *filled_url, char *url, char *user_id, char *lock_id);

esp_err_t client_event_handler(esp_http_client_event_handle_t evt) {
    switch (evt->event_id)
    {
        case HTTP_EVENT_ON_DATA:
            status_code = esp_http_client_get_status_code(client);
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
