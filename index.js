import { firstNames, lastNames, occupations } from "./citizenTools/lists.js";
import { randomArrayItem, minMax } from "./utils/tools.js";

const createPopulace = (pop) => {
    let populace = [];

    for (let i = 0; i < pop + 1; i++) {
        let citizen = {
            firstName: randomArrayItem(firstNames),
            lastName: randomArrayItem(lastNames),
            occupation: randomArrayItem(occupations),
            age: minMax(18, 65),
            species: "Human",
            cash: minMax(10, 1000000),
            alive: true,
            stats: {
                guts: minMax(1, 100),
                sexAppeal: minMax(1, 100),
                occultism: minMax(1, 100),
                vapeSkill: minMax(1, 100),
                kinkyness: minMax(1, 100),
                readingLevel: minMax(1, 12),
                cookiesClear: minMax(0, 1),
                paranoia: minMax(1, 100),
            }
        }
        console.log(citizen)
    }
}

createPopulace(15);
