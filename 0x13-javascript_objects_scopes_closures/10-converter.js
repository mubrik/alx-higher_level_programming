#!/usr/bin/node

function converter (base) {
  return (num) => {
    return num.toString(base);
  };
}

module.exports = {
  converter
};
