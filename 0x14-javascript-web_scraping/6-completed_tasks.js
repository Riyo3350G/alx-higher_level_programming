#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const completedTasks = {};

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed === true) {
        if (completedTasks[todo.userId] === undefined) {
          completedTasks[todo.userId] = 1;
        } else {
          completedTasks[todo.userId] += 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
