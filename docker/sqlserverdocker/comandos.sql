select * from sys.configurations
where name like 'tempdb metadata memory-optimized'

ALTER SERVER CONFIGURATION SET MEMORY_OPTIMIZED TEMPDB_METADATA=ON;