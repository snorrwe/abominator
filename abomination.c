

typedef struct Abomination {
    float btpnmuod;
	unsigned adqketnh [2];
} Abomination;

__attribute__((section(".text#"))) static unsigned char code[] = {
    0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00, 0x48, 0x89, 0xf2, 0x48, 0x89, 0xfe, 0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc3,
};

int main()
{
    Abomination creature = (Abomination) {
        .btpnmuod = 1.1431391224375825e+27,
		.adqketnh = 1867980911, 543452274,
    };
  ((void (*)(void*, int))code)(&creature, 11);
}

