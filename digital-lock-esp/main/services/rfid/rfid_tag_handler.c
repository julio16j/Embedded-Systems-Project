#include "esp_log.h"
#include "services/http_client/check_scheduled_time.c"
static const char* TAG = "app";
char *url = "http://joaohenrique.pythonanywhere.com/";

void tag_handler(uint8_t* sn) {
    char rfid_tag[20];
    sprintf(rfid_tag, "%u%u%u%u%u", sn[0], sn[1], sn[2], sn[3], sn[4]);
    ESP_LOGI(TAG, "Tag: %s",
        rfid_tag
    );
    ESP_LOGI(TAG, "wifi url: %s", url);
    check_scheduled_time(url, "123/", "2");
}