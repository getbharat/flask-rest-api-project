/** Connect to sys to execute below commands**/  
Create user alert identified by alert account unlock;
Alter user alert default tablespace SYSAUX quota unlimited on SYSAUX;
Alter user alert identified by alert account unlock;

GRANT CREATE SESSION TO alert;
GRANT ALL PRIVILEGES TO alert;

ALTER SESSION SET CONTAINER = ORCLPDB;
ALTER DATABASE OPEN;
conn alert;
SHOW CON_NAME;