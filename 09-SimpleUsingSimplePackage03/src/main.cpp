// Hier beginnt und endet die Ausführung des Programms.
//

#include "SEGGER_RTT.h"


int main()
{

  char rttBufferOut[10];
  SEGGER_RTT_printf(0, &rttBufferOut[0]);

  while(true) {
    // Infinite loop to keep the program running
  }
  return 0;
}
