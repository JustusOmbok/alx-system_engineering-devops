#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - allows child processes to be zombies
 * Return: 0 or 1
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("fork");
			return (1);
		}

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}

	infinite_while();
	return (0);
}
