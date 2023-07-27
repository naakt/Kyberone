var today = new Date();
var minute = today.getMinutes()
var second = today.getSeconds();

const a = (minute + 1) * 20
const b = (Math.round(second / 10) + 1)* 10

const exp = a ** b


export default {
    async email(message, env, ctx) {
        if (message.raw) == exp) {