<script lang="ts">
</script>

<div class="Navigation">
	<div class="Navigation__background" />
	<div class="Navigation__FAB" />
	<span />
</div>

<style lang="scss" scoped>
	.Navigation {
		position: relative;
		height: 4rem;

		&__background {
			width: 100%;
			height: 100%;
			background-color: #363636;
			clip-path: polygon(
				calc(50% - 3rem) 0%,
				50% 3rem,
				calc(50% + 3rem) 0%,
				100% 0%,
				100% 100%,
				0% 100%,
				0% 0%
			);
		}

		&__FAB {
			position: absolute;
			background-color: #363636;
			z-index: 9999;

			height: 4rem;
			width: 4rem;

			left: 50%;
			top: 0;

			transform: translate(-50%, -50%);

			clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
		}
	}
</style>
