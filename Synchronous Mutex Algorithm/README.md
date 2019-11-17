## lab1 同步互斥

### Target

1. 掌握进程同步和互斥原理，理解生产者-消费者模型；
2. 学习 Linux 中的多线程并发执行机制；
3. 解决读者－写者问题。

### Basic Concepts

#### Thread

- Thread operations include thread creation，termination，**synchronization(joins,blocking),scheduling**,data management and process interaction.
- A thread **doesn't maintain** a list of created threads,nor does it know the thread that created.
- All threads within a process share the **same address space**.
- Threads in the same process share:
  - Process instructions ( refers to Text segment? )
  - Most data ( Data ,BSS segment... )
  - Opened files ( descriptors )
  - Signals and signal handlers
  - Current working directory
  - User and group IDs
- Each thread has a unique:
  - Thread ID
  - set of registers,stack ptr
  - stack for local varis,rtn adres
  - signal mask
  - priority
  - return value:errno
- pthread functions return "0" if OK

### Just Use It

## 读者与写者问题（reader-writer problem）

有两组并发进程：读者和写者，共享一个文件 F，要求：

1. 允许多个读者可同时对文件执行读操作；
2. 只允许一个写者往文件中写信息；
3. 任一写者在完成写操作之前不允许其他读者或写者工作；
4. 写者执行写操作前，应需已有的写者和读者全部退出。
5. 要求仿真程序产生 3 个读者进程，两个写者进程，读写者都周期性地产生读写要求，读写操作要持续一定时间。
