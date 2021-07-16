using System;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;
using System.IO;

namespace client
{
    class Program
    {
        static bool is_key_send;
        static byte[] ServerpublicKey;
        static RSACryptoServiceProvider rsa = new RSACryptoServiceProvider(2048);
        static void Main(string[] args)
        {
            try
            {
                TcpClient client = new TcpClient("127.0.0.1", 7000);
                Console.WriteLine("Client connected");
                NetworkStream stream = client.GetStream();
                if (is_key_send == false)
                {
                    byte[] bytes_key = new Byte[10000];
                    int key_len = stream.Read(bytes_key, 0, bytes_key.Length);
                    int i = bytes_key.Length - 1;
                    while(bytes_key[i] == 0)
                        --i;
                    byte[] tmpb =  new byte[i+1];
                    Array.Copy(bytes_key, tmpb, i+1);
                    ServerpublicKey = tmpb;
                    is_key_send = true;
                    Console.WriteLine("Public key received");
                }

                while (true)
                {  
                    Console.WriteLine("\nВведите данные");
                    string request = Console.ReadLine();
                    if (request == "exit")
                    {
                        client.Close();
                        Console.WriteLine("\nClient closed");
                    }
                    byte[] SendData = Encoding.ASCII.GetBytes(request);
                    rsa.ImportCspBlob(ServerpublicKey);
                    byte[] encrypted_req = rsa.Encrypt(SendData, false);
                    stream.Write(encrypted_req, 0, encrypted_req.Length);
                    byte[] bytesRead = new byte[256];
                    int len = stream.Read(bytesRead, 0, bytesRead.Length);
                    string answer = Encoding.ASCII.GetString(bytesRead, 0, len);
                    Console.Write(answer); 
                    
                    
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

        }
        static byte[] EncryptStringToBytes_Aes(string plainText, byte[] Key, byte[] IV)
        {
            // Check arguments.
            if (plainText == null || plainText.Length <= 0)
                throw new ArgumentNullException("plainText");
            if (Key == null || Key.Length <= 0)
                throw new ArgumentNullException("Key");
            if (IV == null || IV.Length <= 0)
                throw new ArgumentNullException("IV");
            byte[] encrypted;

            // Create an Aes object
            // with the specified key and IV.
            using (Aes aesAlg = Aes.Create())
            {
                aesAlg.Key = Key;
                aesAlg.IV = IV;

                // Create an encryptor to perform the stream transform.
                ICryptoTransform encryptor = aesAlg.CreateEncryptor(aesAlg.Key, aesAlg.IV);

                // Create the streams used for encryption.
                using (MemoryStream msEncrypt = new MemoryStream())
                {
                    using (CryptoStream csEncrypt = new CryptoStream(msEncrypt, encryptor, CryptoStreamMode.Write))
                    {
                        using (StreamWriter swEncrypt = new StreamWriter(csEncrypt))
                        {
                            //Write all data to the stream.
                            swEncrypt.Write(plainText);
                        }
                        encrypted = msEncrypt.ToArray();
                    }
                }
            }

            // Return the encrypted bytes from the memory stream.
            return encrypted;
        }
        static string DecryptStringFromBytes_Aes(byte[] cipherText, byte[] Key, byte[] IV)
        {
            // Check arguments.
            if (cipherText == null || cipherText.Length <= 0)
                throw new ArgumentNullException("cipherText");
            if (Key == null || Key.Length <= 0)
                throw new ArgumentNullException("Key");
            if (IV == null || IV.Length <= 0)
                throw new ArgumentNullException("IV");

            // Declare the string used to hold
            // the decrypted text.
            string plaintext = null;

            // Create an Aes object
            // with the specified key and IV.
            using (Aes aesAlg = Aes.Create())
            {
                aesAlg.Key = Key;
                aesAlg.IV = IV;

                // Create a decryptor to perform the stream transform.
                ICryptoTransform decryptor = aesAlg.CreateDecryptor(aesAlg.Key, aesAlg.IV);

                // Create the streams used for decryption.
                using (MemoryStream msDecrypt = new MemoryStream(cipherText))
                {
                    using (CryptoStream csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                    {
                        using (StreamReader srDecrypt = new StreamReader(csDecrypt))
                        {

                            // Read the decrypted bytes from the decrypting stream
                            // and place them in a string.
                            plaintext = srDecrypt.ReadToEnd();
                        }
                    }
                }
            }

            return plaintext;
        }
    }
}
