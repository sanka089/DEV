#include <stdio.h>
#include <stdlib.h> // Include this for the rand() function
int main()
{
int buckets, outlets, k = 1, num, remaining;
printf("Enter Bucket size and outstream size\n");
scanf("%d %d", &buckets, &outlets);
remaining = buckets;
while (k)
{
num = rand() % 1000; // Generate a random number between 0 and 999if
(num < remaining)
{
remaining = remaining - num;
printf("Packet of %d bytes accepted\n", num); // Added missing variable
}
else
{
printf("Packet of %d bytes is discarded\n", num);
}
if (buckets - remaining > outlets)
{
remaining += outlets; // Fixed the calculation
}
else
remaining = buckets;
printf("Remaining bytes: %d \n", remaining);
printf("If you want to stop input, press 0, otherwise, press 1\n");
scanf("%d", &k);
}
while (remaining < buckets) // Fixed the condition
{ if (buckets - remaining > outlets)
{
remaining += outlets; // Fixed the calculation
}
else
remaining = buckets;
printf("Remaining bytes: %d \n", remaining);
}
return 0; // Added a return statement to indicate successful completion
}
