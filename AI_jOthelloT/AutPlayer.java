package players;
import java.util.List;
import game.AbstractPlayer;
import game.BoardSquare;
import game.Move;

public class AutPlayer extends AbstractPlayer {
    private  BoardSquare basic_move;
    private  int[][] heuristic_table;
    public AutPlayer(int depth) {
        super(depth);

        heuristic_table=new int[8][];
        heuristic_table[0]=new int[]{4, -3, 2, 2, 2, 2, -3, 4 };
        heuristic_table[1]=new int[]{-3 ,-4, -1, -1, -1, -1, -4, -3  };
        heuristic_table[2]=new int[]{2 ,-1, 1, 0, 0, 1, -1, 2  };
        heuristic_table[3]=new int[]{2, -1, 0, 1, 1, 0, -1, 2  };
        heuristic_table[7]=new int[]{4, -3, 2, 2, 2, 2, -3, 4 };
        heuristic_table[6]=new int[]{-3 ,-4, -1, -1, -1, -1, -4, -3 };
        heuristic_table[5]=new int[]{2 ,-1, 1, 0, 0, 1, -1, 2  };
        heuristic_table[4]=new int[]{2, -1, 0, 1, 1, 0, -1, 2  };


    }

    @Override

    public BoardSquare play(int[][] board) {

        List<Move> possible_moves = getGame().getValidMoves(board, getMyBoardMark());

         basic_move = new BoardSquare(-1, -1); // No Move

        if (possible_moves.size()<1){
            return basic_move;
        }

        int bestMoveMarks = -10001;
        int index_best=0;
        int alpha=-10000;
        int beta=10000;
        int temp=0;
        basic_move=possible_moves.get(0).getBardPlace();
      for (int i=0;i<possible_moves.size();i++){
          int[][] boardCopy = copy(board);
          getGame().do_move(boardCopy, possible_moves.get(i).getBardPlace(), this);
          temp =alphabeta(boardCopy,getOpponentBoardMark(),7,alpha,beta);
          if (temp > bestMoveMarks) {
               bestMoveMarks=temp;
               alpha=temp;
               index_best=i;
              basic_move=possible_moves.get(i).getBardPlace();
          }
      }

        return basic_move;

    }




    private int alphabeta(int[][] board,int board_mark, int depth, int alpha, int beta){
        List<Move> possible_moves = getGame().getValidMoves(board, board_mark);

        if (board_mark==getMyBoardMark() &&  possible_moves.size()==0  ){

            if(    getGame().getValidMoves(board, getOpponentBoardMark()).size()==0  ){return static_evalution(board,1);}

            else{
                if(depth == 0){
                    return static_evalution(board,0);
                }

                return alphabeta(board,getOpponentBoardMark() ,depth, alpha, beta);


            }

        }


        if (board_mark==getOpponentBoardMark() &&  possible_moves.size()==0  ){
            if(    getGame().getValidMoves(board, getMyBoardMark()).size()==0  ){return static_evalution(board,1);}
            else{
                if(depth == 0){
                    return static_evalution(board,0);
                }

                 return alphabeta(board,getMyBoardMark() ,depth, alpha, beta);

            }
        }
        if(depth == 0){
            return static_evalution(board,0);
        }
        int[][] boardCopy ;



        if(board_mark == getMyBoardMark()){
            int temp;
            for(Move child : possible_moves){
                boardCopy = copy(board);
                getGame().do_move(boardCopy, child.getBardPlace(), this);
                 temp = alphabeta(boardCopy,getOpponentBoardMark() ,depth-1, alpha, beta);

                if(alpha < temp){
                    alpha = temp;
                }

                if( beta <= alpha ) {

                    return alpha;

                }
            }

            return alpha;

        }else{
            int temp;

            for(Move child : possible_moves){
                boardCopy = copy(board);
                getGame().do_move(boardCopy, child.getBardPlace(), this);
                 temp = alphabeta(boardCopy,getMyBoardMark() ,depth-1, alpha, beta);
                if(beta > temp){
                    beta = temp;

                }
                if( beta <= alpha ) {
                    return beta;
                }
            }
            return beta;
        }



    }


    private int static_evalution(int[][] board,int fin){

        if(fin==1){
            int nMarks = 0;

            for (int r = 0; r < board.length; r++) {

                for (int c = 0; c < board[0].length; c++) {

                    if (board[r][c] == getMyBoardMark()) {

                        nMarks = nMarks + 1;
                    }else if(board[r][c] == getOpponentBoardMark()){

                        nMarks = nMarks -1;
                    }
                }

            }
             if(nMarks>0)return 10000;

            else if (nMarks<0)return -10000;
             else  return 0;

        }
        else{
           return counter(board);

        }

    }

    private int[][] copy(int[][] board) {

        board = board.clone();

        for (int i = 0; i < board.length; i++) {

            board[i] = board[i].clone();

        }

        return board;

    }



    private int counter(int[][] board) {

        int nMarks = 0;

        for (int r = 0; r < board.length; r++) {

            for (int c = 0; c < board[0].length; c++) {

                if (board[r][c] == getMyBoardMark()) {


                    if((r==0 && c==1 )|| (r==1 && c==0)){

                        if (board[r][c]==getMyBoardMark() && board[0][0]==getMyBoardMark()){

                            heuristic_table[r][c]=3;
                        }
                    }

                    if((r==7 && c==6 )|| (r==6 && c==7)){

                        if (board[r][c]==getMyBoardMark() && board[7][7]==getMyBoardMark()){

                            heuristic_table[r][c]=3;
                        }
                    }
                    if((r==0 && c==6 )|| (r==1 && c==7)){

                        if (board[r][c]==getMyBoardMark() && board[0][7]==getMyBoardMark()){

                            heuristic_table[r][c]=3;
                        }
                    }

                    if((r==6 && c==0 )|| (r==7 && c==1)){

                        if (board[r][c]==getMyBoardMark() && board[7][0]==getMyBoardMark()){

                            heuristic_table[r][c]=3;
                        }
                    }


                    nMarks = nMarks + heuristic_table[r][c];
                }else if(board[r][c] == getOpponentBoardMark()){

                    if((r==0 && c==1 )|| (r==1 && c==0)){

                      if(board[r][c]==getOpponentBoardMark() && board[0][0]==getOpponentBoardMark()){
                            heuristic_table[r][c]=3;
                        }
                    }

                    if((r==7 && c==6 )|| (r==6 && c==7)){

                       if(board[r][c]==getOpponentBoardMark() && board[7][7]==getOpponentBoardMark()){
                            heuristic_table[r][c]=3;
                        }
                    }
                    if((r==0 && c==6 )|| (r==1 && c==7)){

                     if(board[r][c]==getOpponentBoardMark() && board[0][7]==getOpponentBoardMark()){
                            heuristic_table[r][c]=3;
                        }
                    }

                    if((r==6 && c==0 )|| (r==7 && c==1)){

                         if(board[r][c]==getOpponentBoardMark() && board[7][0]==getOpponentBoardMark()){
                            heuristic_table[r][c]=3;
                        }
                    }

                    nMarks = nMarks - heuristic_table[r][c];
                }
            }
        }
        return nMarks;
    }

}