// Предположим, что GS1DigitalLinkToolkit.js находится в той же директории
const GS1DigitalLinkToolkit = require('./GS1DigitalLinkToolkit.js');

const gs1dlt = new GS1DigitalLinkToolkit();

const args = process.argv.slice(2); // Получаем аргументы командной строки
const gtin = args[0]; // GTIN передаётся как первый аргумент

// Здесь ты можешь использовать функции из GS1DigitalLinkToolkit.js для обработки GTIN
// Например:

try {
    // Добавляем GS1 Application Identifier для GTIN, если это необходимо
    // Предполагается, что GTIN уже содержит необходимый AI (например, "(01)")
    const result = gs1dlt.gs1ElementStringsToGS1DigitalLink(gtin, true, null);

    // Выводим результат в stdout в формате JSON
    console.log(JSON.stringify({ url: result }));
} catch (err) {
    // В случае ошибки выводим информацию об ошибке в stderr в формате JSON
    console.error(JSON.stringify({ error: err.message }));
    process.exit(1); // Завершаем выполнение с кодом ошибки
}