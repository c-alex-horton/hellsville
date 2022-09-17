import { firstNames, lastNames, occupations } from "./citizenTools/lists.js";
import { randomArrayItem } from "./utils/tools.js";

const createPopulace = (pop) => {
    let populace = [];

    for (let i = 0; i < pop + 1; i++) {
        let citizen = {
            firstName: randomArrayItem(firstNames),
            lastName: randomArrayItem(lastNames),
            occupation: randomArrayItem(occupations),
            age: Math.floor(Math.random() * (75 - 18) + 18)
        }
        console.log(citizen)
    }
}

createPopulace(5);
