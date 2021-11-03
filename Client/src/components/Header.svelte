<script lang="ts">
	const title = 'Workout';
</script>

<header class="Header">
	<div class="" />
	<h1 class="Header__title">{title}</h1>
	<div class="Header__user" />
</header>

<style lang="scss" scoped>
	.Header {
		background-color: #fff;

		padding: 0.75rem;

		box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);

		display: grid;
		grid-template-columns: 4rem 1fr 4rem;
		place-items: center;

		&__title {
			// text-align: center;
			font-size: 1.5rem;
		}

		&__user {
			background-color: gray;
			border-radius: 9999px;
			width: 2.5rem;
			height: 2.5rem;
		}
	}
</style>
