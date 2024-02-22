#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cstdint>

std::string calculate_param_1(uint param_3, int param_2) {
    std::string param_1;
    uint8_t DAT_00102020[] = {0x4A, 0x3C, 0x66, 0xD0, 0xC7, 0x4B, 0xC6, 0xB7, 0x1B, 0x0D, 0xC0, 0x56, 0xB8, 0xD7, 0xD3, 0x47, 0xB4, 0xE6, 0x67, 0x0E, 0xB6, 0x50, 0x92, 0x8C, 0x22, 0x5C, 0x63, 0x8B, 0x07, 0x09, 0xF6, 0xF1, 0x64, 0x8A, 0x8B, 0xF2, 0x00, 0x00, 0x00, 0x00};
    uint64_t local_38;

    for (int i = 0; i < param_2; i++) {
        uint8_t bVar1 = DAT_00102020[i];
        *(uint8_t *)((long)&local_38 + (long)i) = (uint8_t)param_3 ^ bVar1;
        param_3 = ((param_3 >> 1 | (uint)((param_3 & 1) != 0) << 0x1f) ^ (uint)bVar1) + (param_2 - i);
    }
    std::cout << (char *)&local_38 << std::endl;

    return 0;
}

int main() {
    uint initial_param_3 = 0xbaceb00c;
    int param_2 = 0x24;
    std::string param_1 = calculate_param_1(initial_param_3, param_2);
    std::cout << "Calculated param_1: " << param_1 << std::endl;
    return 0;
}