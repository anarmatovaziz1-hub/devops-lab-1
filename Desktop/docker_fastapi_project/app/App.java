package com.example;
import redis.clients.jedis.Jedis;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import com.sun.net.httpserver.HttpServer;

public class App {
    public static void main(String[] args) throws Exception {
        String redisHost = System.getenv().getOrDefault("REDIS_HOST", "redis");
        Jedis jedis = new Jedis(redisHost, 6379);
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/", (ex) -> {
            long visits = jedis.incr("visits");
            String res = "Salem, Azizbek! Kelushiler sany: " + visits;
            ex.sendResponseHeaders(200, res.length());
            OutputStream os = ex.getResponseBody();
            os.write(res.getBytes());
            os.close();
        });
        server.start();
    }
}