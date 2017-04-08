class test {
	public static void main (String[] args){
		int[] origin = {20, 10, 65, 39, 89, 30, 50};
		createSort(origin, 0, 6);
		for (int i = 0; i <= 6; i++)
		{
			System.out.println(origin[i]);
		}	
	}

	public static int sort(int[] arry, int startP, int endP )
	{
		int fL = startP;
		
		for(int i = startP; i < endP; i++)
		{
			if(arry[i] < arry[endP])
			{
				int temp = arry[i];
				arry[i] = arry[fL];
				arry[fL] = temp;
				fL++;
			}		
		}
		int temp = arry[fL];
                arry[fL] = arry[endP];
                arry[endP] = temp;
		return fL;	
	}

	public static void createSort(int[] arry,int start,  int end)
	{
		int position = sort(arry, start, end);

		if(position != start)
		{
			createSort(arry, start, position - 1);
			
		}

		if(position != end)
		{
			createSort(arry, position + 1, end);
		}	
	}
}
