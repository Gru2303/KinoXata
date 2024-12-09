import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  client: '@hey-api/client-axios',
  input: 'http://127.0.0.1:8000/openapi.json',
  output: {
    format: 'prettier',
    path: './src/client',
  },
  plugins: [
    '@hey-api/schemas',
    '@hey-api/sdk',
    {
      dates: true,
      name: '@hey-api/transformers',
    },
    {
      enums: 'javascript',
      name: '@hey-api/typescript',
    },
  ],
});
