import preprocess from 'svelte-preprocess';
import tsconfigPaths from 'vite-tsconfig-paths';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: preprocess(),

	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',

		vite: {
			plugins: [tsconfigPaths()]
		}
	}
};

export default config;
