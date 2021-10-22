<script lang="ts">
	import 'assets/global.scss';
</script>

<div class="Layout">
	<slot />
</div>

<style lang="scss" scoped>
	.Layout {
		height: 100vh;
		overflow-y: auto;
	}
</style>
