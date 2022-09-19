export const randomArrayItem = (arr) => {
    return arr[Math.floor(Math.random() * arr.length)]
}

export const minMax = (min, max) => {
    return Math.floor(Math.random() * ((max + 1) - min) + min)
}