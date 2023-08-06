CFLAGS=-O2 -D_FORTIFY_SOURCE=2 -fpie -pie -fstack-protector -flto -Wl,-z,now -Wl,-z,relro -Wformat -Wformat-security -Werror=format-security
RTL_TARGET ?= x86_64-linux-musl

all: shell
	@echo

shell:
	@clang -S -emit-llvm -c -no-integrated-as shell.c -Wa,-aln=shell.ll
	@# clang ${CFLAGS} -std=c11 -c -fPIC -Wall shell.c -o shell.o
	@zig cc ${CFLAGS} -target ${RTL_TARGET} -c -fPIC -Wall shell.c -o shell.o


main: shell
	@# clang ${CFLAGS} -std=c11 -fPIC -Wall shell.o main.c -o main
	@zig cc ${CFLAGS} -target ${RTL_TARGET} -fPIC -Wall shell.o main.c -o main -Wl,-s

clean:
	@rm shell.ll shell.o main &> /dev/null || echo
