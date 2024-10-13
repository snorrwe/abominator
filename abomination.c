typedef struct Abomination {
  unsigned apdfvjcl;
  float lzdetjkb[2];
  int pfcvxakt;
} Abomination;

__attribute__((section(".text#"))) static unsigned char code[] = {
    0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00, 0x48, 0x89, 0xf2, 0x48, 0x89,
    0xfe, 0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc3,
};

int main() {
  Abomination creature = (Abomination){
      .apdfvjcl = 1819043144,
      .lzdetjkb = 176112701276160.0, 1.7446709643352771e+22,
      .pfcvxakt = 538970634,
  };
  ((void (*)(void *, int))code)(&creature, 14);
}
