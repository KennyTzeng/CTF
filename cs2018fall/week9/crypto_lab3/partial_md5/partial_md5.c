#include <stdio.h>
#include <openssl/md5.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <fcntl.h>
 
int main(int argc, char **argv)
{
	int fin;
	struct stat st;
	void *p = NULL;
	MD5_CTX ctx;
	unsigned char final[16];
 
	if (argv[1] == NULL) {
		printf("./partial_md5 </path/to/file>\n");
		exit(-1);
	}
 
	fin = open(argv[1], O_RDONLY);
	if (fin < 0 ) {
		printf("Can't open %s\n", argv[1]);
		exit(-1);
	}
	stat(argv[1], &st);
	if (st.st_size % 64 != 0) {
		printf("Filesize is not a multiple of blocksize (64B)!\n");
		printf("Pad it with %ld more bytes!\n", 64 - (st.st_size % 64) );
		exit(-1);
	}
 
	p = mmap(NULL, st.st_size, PROT_READ, MAP_PRIVATE, fin, 0);
	if (!p) {
		printf("Mmap failed\n");
		exit(-1);
	}
 
	MD5_Init(&ctx);
	MD5_Update(&ctx, p, st.st_size);
 
	printf("Partial MD5 is %08X %08X %08X %08X\n", ctx.A, ctx.B, ctx.C, ctx.D);
	MD5_Final(final, &ctx);
 
	printf("Final MD5 is %08X %08X %08X %08X\n", ctx.A, ctx.B, ctx.C, ctx.D);
 
	return 0;
}
