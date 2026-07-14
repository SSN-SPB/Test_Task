import js from '@eslint/js';
import globals from 'globals';
import prettier from 'eslint-config-prettier';

export default [
    js.configs.recommended,

    {
        files: ['**/*.js'],

        ignores: ['node_modules/**', 'cypress/videos/**', 'cypress/screenshots/**'],

        languageOptions: {
            ecmaVersion: 'latest',

            sourceType: 'module',

            globals: {
                ...globals.browser,
                ...globals.node,
            },
        },

        rules: {
            'no-var': 'error',

            'prefer-const': 'error',

            eqeqeq: ['error', 'always'],

            'no-unused-vars': [
                'warn',
                {
                    argsIgnorePattern: '^_',
                },
            ],
        },
    },

    prettier,
];
