#!/usr/bin/yarn dev
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value);
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(`${reply}`);
  } catch (err) {
    console.log('Error retrieving value:', err.toString());
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

