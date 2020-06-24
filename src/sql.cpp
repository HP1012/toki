#include <stdio.h>
#include <stdlib.h>
#include "libsqlite3/sqlite3.h"

static int callback(void *NotUsed, int argc, char **argv, char **azColName) {
   int i;
   for(i = 0; i<argc; i++) {
      printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
   }
   printf("\n");
   return 0;
}

int insert_database(int id,const char name[],int age,const char address[],int salary){
   sqlite3 *db;
   char *zErrMsg = 0;
   int rc;
   char *sql = (char*)malloc(10000);

   /* Open database */
   rc = sqlite3_open("db/demo.db", &db);
   
   if( rc ) {
      fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
      return(0);
   } else {
      fprintf(stderr, "Opened database successfully\n");
   }

   /* Create SQL statement */
   //   sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
   //       "VALUES (8, 'phiqaw', 32, 'California', 20000.00 );";

   fprintf(stderr,"Create SQL statement\n");
   sprintf(sql,"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) "  \
         "VALUES (%d, \'%s\', %d, \'%s\', %d );",id,name,age,address,salary);
   fprintf(stderr,"%s\n",sql);
   /* Execute SQL statement */
   rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);
   free(sql);
   if( rc != SQLITE_OK ){
      fprintf(stderr, "SQL error: %s\n", zErrMsg);
      sqlite3_free(zErrMsg);
   } else {
      fprintf(stdout, "Records created successfully\n");
   }
   sqlite3_close(db);

   return 1;
}

int main(int argc, char* argv[]) {
   int tmp = insert_database(1,"phi",24,"VietNam",500);
   return 0;
}

extern "C"{
   int cffi_insert_database(int id,const char name[],int age,const char address[],int salary){
      int tmp = insert_database(id,name,age,address,salary);
      return tmp;
   }
}