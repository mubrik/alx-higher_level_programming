#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let occur = 0;
  list.forEach(_elem => {
    if (_elem === searchElement) {
      ++occur;
    }
  });

  return occur;
}

module.exports = {
  nbOccurences
};
