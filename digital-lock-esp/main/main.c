#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/timers.h"
#include "freertos/event_groups.h"
#include "config/wifi_configuration.c"
#include "http_client/check_scheduled_time.c"

#define default_string_size 50

char wifi_ssid[ssid_size] = "wifi1";
char wifi_password[password_size] = "12345678";
char *url = "http://joaohenrique.pythonanywhere.com/";

void app_main(void)
{
    wifi_init(wifi_ssid, wifi_password);
    vTaskDelay(5000 / portTICK_PERIOD_MS);
    check_scheduled_time(url, "123/", "1");
}
