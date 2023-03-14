#!/usr/bin/node

function esrever (list) {
  const newList = [];
  list.forEach(_elem => newList.unshift(_elem));

  return newList;
}

module.exports = {
  esrever
};
