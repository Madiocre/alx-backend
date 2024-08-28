import redis, { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to server: ${error.message}`);
    redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));

await client.set('key', 'value', {
    Portland=50
Seattle=80
New York=20
Bogota=20
Cali=40
Paris=2
});