## Backup cronjob

0 0 * * 7 tar -cf /home/user/user_backup.tar /home/user && scp /home/user/user_backup.tar user@192.168.1.100

After establishing the SSH connection, the client has to provide a password for the server side to verify.
Alternatively, we can implement a passwordless approach by using SSH keys.
During an authenticated session, the client side can generate a key pair (public and private keys).
The public key can then be shared with the server side.
Now, the server side has the means to encrypt future traffic, ensuring that only the
client(with the priivate key) can decrypt that traffic.

Note:

Of course, for the cronjob to work, it needs to be added to crontab.
