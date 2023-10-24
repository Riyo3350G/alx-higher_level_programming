#!/usr/bin/node
const fs = require('fs');
const file_path = process.argv[2];
const content = process.argv[3];

fs.writeFileSync(file_path, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
