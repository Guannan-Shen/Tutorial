#### Set Up SSH connection to Google Cloud Platform (GCP) Computing Console
##### [First Time](#head1)
##### [Daily Connection](#head2)
##### [Local Server Yampa](#head3)
##### [SFTP via FileZilla](#head4)

#### <a name="head1"></a>First Time for GCP [The reference youtube video](https://www.youtube.com/watch?v=R8C66NwMJLs&t=0s&list=WL&index=2)

1. **open** my git bash in Windows, which comes with the **Git for Windows** (Jump to step 3 if you haven't used any SSH before)
2. cd to (or mkdir first of ~/.ssh), **cd ~/.ssh/**
3. **ssh-keygen -t rsa -f ~/.ssh/gc_rsa -C username** (username of the campus). This is to generate public/private Key pair
4. during the previous step, enter your own **passphrase**
5. **ls** under ~/.ssh
6. Make sure there is **gc_rsa.pub**, keep this terminal 
7. Open the GC console, left drop-down menu, the **compute engine**, **VM Instances**
8. Double click an instance. **instance details**, **Edit**
9. Go to **You have SSH Keys**, **Add item**
10. In the previous terminal, **vi gc_rsa.pub**
11. **Copy** the whole ssh-rsa till your username. **Ctrl Z** to exit the view. 
12. In the gc console, **SSH Keys**, **Add item**, **paste** the public key. 
13. In the terminal, **nano ~/.bashrc**
14. paste these software (bowtie, samtools, RSEM, hisat2) into the PATH
    
    export PATH=$PATH:/Users/harry/.local/bin/cutadapt

    export PATH PATH=$PATH:$HOME/.local/bin:$HOME/bin://home/harry/sourceCode/bowtie2-2.3.3

    export PATH PATH=$PATH:$HOME/.local/bin:$HOME/bin://home/harry/sourceCode/samtools-1.5

    export PATH PATH=$PATH:$HOME/.local/bin:$HOME/bin://home/harry/sourceCode/RSEM-1.3.0

    export PATH PATH=$PATH:$HOME/.local/bin:$HOME/bin://home/harry/sourceCode/hisat2-0f01dc6397a
    
15. In the terminal, check **hisat2 --version** to test if softwares are loaded properly

#### <a name="head2"></a>Connect the GC each time when you need GC, yes during the process

1. **open** git bash (Windows)
2. **cd ~/.ssh/**
3. **chmod 400 gc_rsa** This is to change the permission on private key.
4. Go to the **compute engine**, **VM Instances**, **Check the box** (for the instance you use)
5. **start** to get the *external IP*
6. In the terminal, connect to the GC by **ssh -i gc_rsa username@externalIP**
7. The raw data is saved in GC, **Storage**, **Browser**, the *bucket*
8. Now when you need the data, mount the bucket into your gc console.
9. **gcsfuse --file-mode 777 --dir-mode 777 --implicit-dirs bidump001 /home/username/yourfolder/yourbucketfolder**
10. Success if **File system has been successfully mounted**


##### <a name="head3"></a>For the local server Yampa
1. In the git bash, **ssh username@yampa.ucdenver.pvt**
2. yes
3. the password, nIcHistaY4

#### <a name="head4"></a>SFTP via FileZilla
This is for download file from remote server, upload to GCP is easy **just Drag**
1. Download free version of FileZilla client for Wins 64bit
2. In the Edit > settings, find SFTP, add key file
3. choose the key file **gc_rsa** in ~/.ssh folder(~stands for /home/user), transfer to **gc_rsa.ppk** and save it in the default folder
4. In site manager, upper left corner under the file option, new site
5. Protocol as SFTP, Host is the external IP of GCP instance, Logon Type as Key file, User is your User name, Key file is the **gc_rsa.ppk**, click connect
6. left panel is local, right panel is remote server 








