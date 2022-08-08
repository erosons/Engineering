Hadoop (Google file system)
 - HDFS -hadoop distributed file system
 - MR- map reduce
   
   Hadoop  FrameWork
       - Hadoop storage cluster : https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.htmlclear
	   
       - Hive 
       - squoop
           - For import and export of data to and fro HDFS - RDMS
       - Flume 
          - For import and export of data to and fro HDFS - Network attached storage
       - Command 
	       Leave Safe Mode for Hadoop which can restrict various operations in hadoop

            >> hdfs dfsadmin -safemode leave  OR bin/hadoop dfsadmin -safemode leave

            >> Hadoop distcp  for copying file from Cluster1 to Cluster2 Namenode to another Namenode
          Shell Command:
		    >> Start hadoop cluster : sbin/stop-dfs.sh
			>> Stop hadoop Cluster: sbin/start-yarn.sh
		    >>  hdfs dfs fsck /  OR hadoop fsck / => To disk distribution
			>>  hdfs    dfs -ls / OR  hadoop fs -ls hdfs:/   => to list current directory
			>>  hdfs    dfs - mkdir /DW  OR hadoop fs -mkdir hdfs:/testfolder  => To create a new directory
			>>  hadoop  fs -put(-copyFromLocal) /home/samson/HelloWord.py hdfs:/Directory
			>>  hadoop  fs -get(-copyToLocal)  hdfs:/Directory/HelloWord.py /home/samson/
			>>  hadoop  fs -ls hdfs:///output-folder1/
            >>  hadoop  fs -copyFromLocal
            >>  hadoop  fs -cp
			>>  hdfs dfs -touchz /DW/HelloWorld.py or  hadoop fs -touchz hdfs:/DW/HelloWord2.py   => create a file
			>>  hdfs dfs -du -s /DW/HelloWorld.py   => Check size of a file
			>>  hdfs dfs -appendTofile - /DW/HelloWorld.py
			       This allows you to add content to your file
				   Crtl + D => When you finish
            >>
        Copy from S3 to HDFS directory                  
          >> hadoop distcp s3:path.parquet  /directory

        Copy to and fro EMR cluster 
         Ensure S3DistCp is added at the launch step of the EMR :
            -  https://aws.amazon.com/premiumsupport/knowledge-center/copy-s3-hdfs-emr/
            - https://aws.amazon.com/blogs/big-data/seven-tips-for-using-s3distcp-on-amazon-emr-to-move-data-efficiently-between-hdfs-and-amazon-s3/

          >> s3-dist-cp --src /data/incoming/hourly_table --dest s3://my-tables/incoming/hourly_table
          >> s3-dist-cp --src s3://my-tables/incoming/hourly_table --dest s3://my-tables/incoming/hourly_table_archive --deleteOnSuccess
         
        Copy and change file compression on the fly
          >> s3-dist-cp --src s3://my-tables/incoming/hourly_table_filtered --dest s3://my-tables/incoming/hourly_table_gz --outputCodec=gz
               The current version of S3DistCp supports the codecs gzip, gz, lzo, lzop, and snappy, and the keywords none and keep (the default). These keywords have the following meaning:
        
        Adding s3distCp to a runinng EMR Cluster
            https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UsingEMR_s3distcp.html#UsingEMR_s3distcp.step

       - scp,ftp
             for file transfer protocol
       - HUE
           - To load data from file browser to HDFS
       - JAVA API
           - to read and write files on HDFS
          
  

       - Ozie

What is a file System 
  : is a method and data structure that the operating system uses to control how data is stored and retrieved.[
     A file system consists of two or three layers. Sometimes the layers are explicitly separated, and sometimes the functions are combined
Logical file system :
    is responsible for interaction with the user application. 
    It provides the application program interface (API) for file operations — OPEN, CLOSE, READ
  
Types of Filesystems based various Operating system
   NTFS (standalone) used by windows - New technology file system
   EXT (standalone) used by linux - extensible file system
   HDFS (distributed)- hadoop file system
   s3 (distributed) -simple storage service
   Apple File System (APFS), the default file system for Mac computers 
 
 Standlone in this context, data stored in one NTFS machine , despite the fact the topology of the infrstructure is the distribued
 Distributed context: data is distributed across all NTFS Node and the Node infrasture is also clustered.
 
 ------ 
 Block  
 ======
   this is a unit or piece from the spliting of bulk data by the file system into multiple parts called blocks in a hard disk
   Benefits: this allows for easy retrieval data from the HDD without consuming alot of time.
    
    NTFS - standard default cluster size 4KB block size.  


Usage: hadoop fs [generic options]
	[-appendToFile <localsrc> ... <dst>]
	[-cat [-ignoreCrc] <src> ...]
	[-checksum [-v] <src> ...]
	[-chgrp [-R] GROUP PATH...]
	[-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
	[-chown [-R] [OWNER][:[GROUP]] PATH...]
	[-concat <target path> <src path> <src path> ...]
	[-copyFromLocal [-f] [-p] [-l] [-d] [-t <thread count>] [-q <thread pool queue size>] <localsrc> ... <dst>]
	[-copyToLocal [-f] [-p] [-crc] [-ignoreCrc] [-t <thread count>] [-q <thread pool queue size>] <src> ... <localdst>]
	[-count [-q] [-h] [-v] [-t [<storage type>]] [-u] [-x] [-e] [-s] <path> ...]
	[-cp [-f] [-p | -p[topax]] [-d] [-t <thread count>] [-q <thread pool queue size>] <src> ... <dst>]
	[-createSnapshot <snapshotDir> [<snapshotName>]]
	[-deleteSnapshot <snapshotDir> <snapshotName>]
	[-df [-h] [<path> ...]]
	[-du [-s] [-h] [-v] [-x] <path> ...]
	[-expunge [-immediate] [-fs <path>]]
	[-find <path> ... <expression> ...]
	[-get [-f] [-p] [-crc] [-ignoreCrc] [-t <thread count>] [-q <thread pool queue size>] <src> ... <localdst>]
	[-getfacl [-R] <path>]
	[-getfattr [-R] {-n name | -d} [-e en] <path>]
	[-getmerge [-nl] [-skip-empty-file] <src> <localdst>]
	[-head <file>]
	[-help [cmd ...]]
	[-ls [-C] [-d] [-h] [-q] [-R] [-t] [-S] [-r] [-u] [-e] [<path> ...]]
	[-mkdir [-p] <path> ...]
	[-moveFromLocal [-f] [-p] [-l] [-d] <localsrc> ... <dst>]
	[-moveToLocal <src> <localdst>]
	[-mv <src> ... <dst>]
	[-put [-f] [-p] [-l] [-d] [-t <thread count>] [-q <thread pool queue size>] <localsrc> ... <dst>]
	[-renameSnapshot <snapshotDir> <oldName> <newName>]
	[-rm [-f] [-r|-R] [-skipTrash] [-safely] <src> ...]
	[-rmdir [--ignore-fail-on-non-empty] <dir> ...]
	[-setfacl [-R] [{-b|-k} {-m|-x <acl_spec>} <path>]|[--set <acl_spec> <path>]]
	[-setfattr {-n name [-v value] | -x name} <path>]
	[-setrep [-R] [-w] <rep> <path> ...]
	[-stat [format] <path> ...]
	[-tail [-f] [-s <sleep interval>] <file>]
	[-test -[defswrz] <path>]
	[-text [-ignoreCrc] <src> ...]
	[-touch [-a] [-m] [-t TIMESTAMP (yyyyMMdd:HHmmss) ] [-c] <path> ...]
	[-touchz <path> ...]
	[-truncate [-w] <length> <path> ...]
	[-usage [cmd ...]]


EMR cluster on aws    => Using  S3DistCp  Utility
=====================

https://aws.amazon.com/blogs/big-data/seven-tips-for-using-s3distcp-on-amazon-emr-to-move-data-efficiently-between-hdfs-and-amazon-s3/


Dealing : Cluster not in sync

Ensure Cluster in ->  cat /hadoop3-dir/namenode-dir/current/VERSION sync with the 

Cluster ID->  cat /hadoop3-dir/datanode-dir/current/VERSION 
