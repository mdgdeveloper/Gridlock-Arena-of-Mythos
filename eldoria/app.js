// Data retrieval 
// Fetch the content https://raw.githubusercontent.com/microsoft/CopilotAdventures/main/Data/scrolls.txt location.
// The content will be in text format.

// Fetch the content from the URL
fetch('https://raw.githubusercontent.com/microsoft/CopilotAdventures/main/Data/scrolls.txt')
    .then(response => response.text())
    .then(data => {
        const content = data;
// The scroll contains both the Elders' secrets and misleading information.
// The true secrets have a specific pattern: they are always surrounded by the symbols {* and *}.
// Extract all the true secrets from the scroll.

// Use regex to find all the secrets
const regex = /\{\*(.*?)\*\}/g;

// Store all the secrets in an array
const secrets = content.match(regex);

// Remove the symbols from the secrets
/**
 * Removes symbols from each secret in the array.
 *
 * @param {string[]} secrets - The array of secrets.
 * @returns {string[]} - The array of secrets without symbols.
 */
const secretsWithoutSymbols = secrets.map(secret => secret.replace(/\{\*/g, '').replace(/\*\}/g, ''));

// Display the extracted secrets in a structured manner.
// Ensure that no misleading information is displayed.

console.log(secretsWithoutSymbols);
    })
    .catch(error => console.error('Error:', error));




