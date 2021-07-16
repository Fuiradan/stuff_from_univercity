using System;
using System.Net;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;



namespace server
{
    class Program
    {
        static byte[] privateKey;
        static byte[] publicKey;
        static bool is_key_send;
        static RSACryptoServiceProvider rsa = new RSACryptoServiceProvider(2048);
        static Tuple <byte[], byte[]> GenerateRSAKeys()
        {
            
            byte[] PrivateKey = rsa.ExportCspBlob(true);
            byte[] PublicKey = rsa.ExportCspBlob(false);
            return new Tuple<byte[], byte[]>(PrivateKey, PublicKey);
        }
        static void Main(string[] args)
        {
            var tmp = GenerateRSAKeys();
            privateKey = tmp.Item1;
            publicKey = tmp.Item2; 
            try 
            {
                TcpListener serverSocket = new TcpListener(IPAddress.Any, 7000);
                serverSocket.Start();
                Console.WriteLine("Server started");
                TcpClient clientSocket = serverSocket.AcceptTcpClient();
                NetworkStream stream = clientSocket.GetStream();
                if (is_key_send == false)
                {
                    stream.Write(publicKey, 0, publicKey.Length);
                    is_key_send = true;
                    Console.WriteLine("Public key send to client");
                }
                while (true)
                {
                    byte[] bytes = new byte[10000];
                    int len = stream.Read(bytes, 0, bytes.Length);
                    int i = bytes.Length - 1;
                    while(bytes[i] == 0)
                        --i;
                    byte[] tmpb =  new byte[i+1];
                    Array.Copy(bytes, tmpb, i+1);
                    string encrypted_s = Encoding.ASCII.GetString(tmpb, 0, tmpb.Length);
                    Console.WriteLine(encrypted_s);
                    byte[] data = rsa.Decrypt(tmpb, false);
                    string request = Encoding.ASCII.GetString(data, 0, data.Length);
                    Console.Write("Got request: " + request);

                    string message = "Length: " + request.Length;
                    byte[] bytes_n = Encoding.ASCII.GetBytes(message);
                    stream.Write(bytes_n, 0, bytes_n.Length);

                }
                clientSocket.Close();
                serverSocket.Stop();
                Console.WriteLine("Server stopped");
            }
            catch (Exception e)
            {
              Console.WriteLine(e.Message);  
            }
            Console.ReadKey();
        }
    }
}