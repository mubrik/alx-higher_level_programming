#!/usr/bin/node

function addMeMaybe (num, func) {
  func(++num);
}

module.exports = {
  addMeMaybe
};
