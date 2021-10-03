import java.util.concurrent.Semaphore;

class ReaderWriter {

    static Semaphore readLock = new Semaphore(1);
    static Semaphore writeLock = new Semaphore(1);
    static int readCount = 0;

    static class Read implements Runnable {
        @Override
        public void run() {
            try {
                readLock.acquire();
                readCount++;
                if (readCount == 1) {
                    writeLock.acquire();
                }
                readLock.release();

                System.out.println("Thread " + Thread.currentThread().getName() + " is reading.");
                Thread.sleep(1500);
                System.out.println("Thread " + Thread.currentThread().getName() + " has finished reading.");

                readLock.acquire();
                readCount--;
                if (readCount == 0) {
                    writeLock.release();
                }
                readLock.release();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    static class Write implements Runnable {
        @Override
        public void run() {
            try {
                writeLock.acquire();
                System.out.println("Thread " + Thread.currentThread().getName() + " is writing.");
                Thread.sleep(2500);
                System.out.println("Thread " + Thread.currentThread().getName() + " has finished writing.");
                writeLock.release();
            } catch (InterruptedException e) {
                System.out.println(e.getMessage());
            }
        }
    }

    public static void main(String[] args) throws Exception {
        Read read = new Read();
        Write write = new Write();
        Thread t1 = new Thread(read);
        t1.setName("1");
        Thread t2 = new Thread(read);
        t2.setName("2");
        Thread t3 = new Thread(write);
        t3.setName("3");
        Thread t4 = new Thread(read);
        t4.setName("4");
        t1.start();
        t3.start();
        t2.start();
        t4.start();
    }
}