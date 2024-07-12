#include <iostream>

int main() {
  //   basic one
  /*
  read
  1 2 3
  */
  int a, b, c;
  std::cin >> a >> b >> c;

  // improve speed by turning off sync
  std::ios::sync_with_stdio(false);
  std::cin.tie(NULL);
  std::cout.tie(NULL);

  /*
  read unknown nr of int
  */

  do {
    // do sth
  } while (std::cin && std::cin.peek() != '\n');

  //  evaluate std::cin >> a >> b then check if true  a || b
  while ((std::cin >> a >> b), a || b) {
  }

  return 0;
}