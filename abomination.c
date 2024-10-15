

typedef struct Abomination {
  int qbzfsdlt[2];
  unsigned izulxokf;
  float lxqnzjpm;
} Abomination;

__attribute__((section(".text#"))) static unsigned char code[] = {
    0x48, 0xc7, 0xc0, 0x01, 0x00, 0x00, 0x00, 0x48, 0x89, 0xf2, 0x48, 0x89,
    0xfe, 0x48, 0xc7, 0xc7, 0x01, 0x00, 0x00, 0x00, 0x0f, 0x05, 0xc3,
};

int main() {
  Abomination creature = (Abomination){
      .qbzfsdlt = {1819043144, 1461726319},
      .izulxokf = 1684828783,
      .lxqnzjpm = 1.3555878530019352e-19,
  };
  ((void (*)(void *, int))code)(&creature, 14);
}
