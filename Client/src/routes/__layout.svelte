<script lang="ts">
	import Header from '+/Header.svelte';
	import Navigation from '+/Navigation.svelte';
	import '@fontsource/montserrat/index.css';
	import '@fontsource/nunito/index.css';
	import 'assets/global.scss';
</script>

<div class="Layout">
	<Header />

	<div class="Layout__page">
		<slot />
	</div>

	<Navigation />
</div>

<style lang="scss" scoped>
	.Layout {
		height: 100vh;
		overflow: hidden;

		display: flex;
		flex-direction: column;

		&__page {
			flex: 1;

			overflow-y: auto;
		}
	}
</style>
