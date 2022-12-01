#include <stdio.h>
#include "rc522.h"
#include "config/wifi_configuration.c"
#include "config/rfid_configuration.c"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/timers.h"
#include "freertos/event_groups.h"
#define default_string_size 50

void app_main(void)
{
    wifi_init(wifi_ssid, wifi_password);
    rc522_start(rfid_configuration_args);
}
