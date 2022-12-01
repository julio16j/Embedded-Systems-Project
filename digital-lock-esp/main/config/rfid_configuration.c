#include "services/rfid/rfid_tag_handler.c"
const rc522_start_args_t rfid_configuration_args = {
    .miso_io  = 4,
    .mosi_io  = 23,
    .sck_io   = 19,
    .sda_io   = 22,
    .callback = &tag_handler,
};